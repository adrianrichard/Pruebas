const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json({ limit: '10mb' }));
app.use(express.static('public'));

const DB_PATH = path.join(__dirname, 'db.json');

// Leer la base de datos JSON
function readDB() {
    try {
        if (!fs.existsSync(DB_PATH)) {
            console.log('❌ db.json no encontrado, creando uno por defecto...');
            const defaultDB = {
                parroquias: [
                    {
                        "id": 1,
                        "nombre": "Parroquia San Miguel Arcángel",
                        "direccion": "Calle Principal 123",
                        "telefono": "011-1234-5678"
                    },
                    {
                        "id": 2,
                        "nombre": "Nuestra Señora del Rosario",
                        "direccion": "Av. Central 456",
                        "telefono": "011-2345-6789"
                    }
                ],
                horarios: [
                    {"parroquia_id": 1, "dia_semana": 1, "hora": "09:00"},
                    {"parroquia_id": 1, "dia_semana": 1, "hora": "18:30"},
                    {"parroquia_id": 2, "dia_semana": 1, "hora": "09:00"}
                ]
            };
            writeDB(defaultDB);
            return defaultDB;
        }
        const data = fs.readFileSync(DB_PATH, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        console.error('Error leyendo DB:', error);
        return { parroquias: [], horarios: [] };
    }
}

// Guardar la base de datos JSON
function writeDB(data) {
    try {
        fs.writeFileSync(DB_PATH, JSON.stringify(data, null, 2), 'utf8');
        console.log('✅ Datos guardados correctamente');
        return true;
    } catch (error) {
        console.error('Error guardando DB:', error);
        return false;
    }
}

// ============ RUTAS PRINCIPALES ============

// Ruta principal
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/admin.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'admin.html'));
});

// ============ API PÚBLICA ============

// Obtener horarios del día actual
app.get('/api/horarios', (req, res) => {
    try {
        const hoy = new Date();
        const diaSemana = hoy.getDay();
        const db = readDB();
        
        console.log(`📅 Consultando horarios para día ${diaSemana} (${hoy.toLocaleDateString()})`);
        
        const horariosDia = db.horarios.filter(h => h.dia_semana === diaSemana);
        
        const horariosAgrupados = {};
        horariosDia.forEach(horario => {
            if (!horariosAgrupados[horario.hora]) {
                horariosAgrupados[horario.hora] = [];
            }
            
            const parroquia = db.parroquias.find(p => p.id === horario.parroquia_id);
            if (parroquia) {
                horariosAgrupados[horario.hora].push({
                    id: parroquia.id,
                    nombre: parroquia.nombre
                });
            }
        });
        
        const horarios = Object.keys(horariosAgrupados)
            .sort((a, b) => a.localeCompare(b))
            .map(hora => ({
                hora: hora,
                parroquias: horariosAgrupados[hora].map(p => p.nombre),
                parroquias_ids: horariosAgrupados[hora].map(p => p.id)
            }));
        
        res.json({
            success: true,
            fecha: hoy.toISOString(),
            dia_semana: diaSemana,
            horarios: horarios
        });
    } catch (err) {
        console.error('Error:', err);
        res.status(500).json({ success: false, error: err.message });
    }
});

// Obtener todas las parroquias
app.get('/api/parroquias', (req, res) => {
    try {
        const db = readDB();
        console.log(`📋 Enviando ${db.parroquias.length} parroquias`);
        res.json(db.parroquias);
    } catch (err) {
        console.error('Error:', err);
        res.status(500).json({ success: false, error: err.message });
    }
});

// Obtener una parroquia específica
app.get('/api/parroquia/:id', (req, res) => {
    try {
        const db = readDB();
        const id = parseInt(req.params.id);
        const parroquia = db.parroquias.find(p => p.id === id);
        
        if (!parroquia) {
            res.status(404).json({ success: false, error: 'Parroquia no encontrada' });
            return;
        }
        
        res.json(parroquia);
    } catch (err) {
        res.status(500).json({ success: false, error: err.message });
    }
});

// ============ API ADMINISTRACIÓN ============

// Obtener todos los datos (para admin)
app.get('/api/admin/datos', (req, res) => {
    try {
        const db = readDB();
        console.log('🔧 Enviando datos completos a admin');
        res.json(db);
    } catch (err) {
        console.error('Error:', err);
        res.status(500).json({ success: false, error: err.message });
    }
});

// Guardar todos los datos
app.post('/api/admin/guardar', (req, res) => {
    try {
        const nuevosDatos = req.body;
        
        if (!nuevosDatos.parroquias) {
            res.status(400).json({ success: false, error: 'Estructura de datos inválida' });
            return;
        }
        
        if (!nuevosDatos.horarios) {
            nuevosDatos.horarios = [];
        }
        
        if (writeDB(nuevosDatos)) {
            console.log('💾 Datos guardados desde admin');
            res.json({ success: true, message: 'Datos guardados correctamente' });
        } else {
            res.status(500).json({ success: false, error: 'Error al guardar' });
        }
    } catch (err) {
        console.error('Error:', err);
        res.status(500).json({ success: false, error: err.message });
    }
});

// Agregar parroquia
app.post('/api/admin/parroquias', (req, res) => {
    try {
        const db = readDB();
        const nuevaParroquia = req.body;
        
        const maxId = db.parroquias.length > 0 ? Math.max(...db.parroquias.map(p => p.id)) : 0;
        nuevaParroquia.id = maxId + 1;
        
        db.parroquias.push(nuevaParroquia);
        
        if (writeDB(db)) {
            console.log(`✅ Parroquia agregada: ${nuevaParroquia.nombre} (ID: ${nuevaParroquia.id})`);
            res.json({ success: true, parroquia: nuevaParroquia });
        } else {
            res.status(500).json({ success: false, error: 'Error al guardar' });
        }
    } catch (err) {
        console.error('Error:', err);
        res.status(500).json({ success: false, error: err.message });
    }
});

// Actualizar parroquia
app.put('/api/admin/parroquias/:id', (req, res) => {
    try {
        const db = readDB();
        const id = parseInt(req.params.id);
        const index = db.parroquias.findIndex(p => p.id === id);
        
        if (index === -1) {
            res.status(404).json({ success: false, error: 'Parroquia no encontrada' });
            return;
        }
        
        db.parroquias[index] = { ...db.parroquias[index], ...req.body, id };
        
        if (writeDB(db)) {
            console.log(`✏️ Parroquia actualizada: ${db.parroquias[index].nombre}`);
            res.json({ success: true, parroquia: db.parroquias[index] });
        } else {
            res.status(500).json({ success: false, error: 'Error al guardar' });
        }
    } catch (err) {
        res.status(500).json({ success: false, error: err.message });
    }
});

// Eliminar parroquia
app.delete('/api/admin/parroquias/:id', (req, res) => {
    try {
        const db = readDB();
        const id = parseInt(req.params.id);
        
        db.parroquias = db.parroquias.filter(p => p.id !== id);
        db.horarios = db.horarios.filter(h => h.parroquia_id !== id);
        
        if (writeDB(db)) {
            console.log(`🗑️ Parroquia eliminada (ID: ${id})`);
            res.json({ success: true, message: 'Parroquia eliminada' });
        } else {
            res.status(500).json({ success: false, error: 'Error al guardar' });
        }
    } catch (err) {
        res.status(500).json({ success: false, error: err.message });
    }
});

// Agregar horario
app.post('/api/admin/horarios', (req, res) => {
    try {
        const db = readDB();
        const nuevoHorario = req.body;
        
        db.horarios.push(nuevoHorario);
        
        if (writeDB(db)) {
            console.log(`✅ Horario agregado: Parroquia ID ${nuevoHorario.parroquia_id} - ${nuevoHorario.hora}`);
            res.json({ success: true, horario: nuevoHorario });
        } else {
            res.status(500).json({ success: false, error: 'Error al guardar' });
        }
    } catch (err) {
        console.error('Error:', err);
        res.status(500).json({ success: false, error: err.message });
    }
});

// Eliminar horario
app.delete('/api/admin/horarios/:index', (req, res) => {
    try {
        const db = readDB();
        const index = parseInt(req.params.index);
        
        if (index >= 0 && index < db.horarios.length) {
            const horarioEliminado = db.horarios[index];
            db.horarios.splice(index, 1);
            
            if (writeDB(db)) {
                console.log(`🗑️ Horario eliminado: ${horarioEliminado.hora}`);
                res.json({ success: true });
            } else {
                res.status(500).json({ success: false, error: 'Error al guardar' });
            }
        } else {
            res.status(404).json({ success: false, error: 'Horario no encontrado' });
        }
    } catch (err) {
        res.status(500).json({ success: false, error: err.message });
    }
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`\n🚀 ========================================`);
    console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
    console.log(`📁 Archivo de datos: ${DB_PATH}`);
    console.log(`📅 Hoy es ${new Date().toLocaleDateString('es-ES', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}`);
    console.log(`🔧 Panel admin: http://localhost:${PORT}/admin.html`);
    console.log(`🚀 ========================================\n`);
});
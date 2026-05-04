const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Leer la base de datos JSON
function readDB() {
    const data = fs.readFileSync(path.join(__dirname, 'db.json'), 'utf8');
    return JSON.parse(data);
}

// Endpoint para obtener horarios del día actual
app.get('/api/horarios', (req, res) => {
    try {
        const hoy = new Date();
        const diaSemana = hoy.getDay(); // 0=Domingo, 1=Lunes, ..., 6=Sábado
        
        const db = readDB();
        
        // Filtrar horarios por día de semana
        const horariosDia = db.horarios.filter(h => h.dia_semana === diaSemana);
        
        // Agrupar por hora
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
        
        // Convertir a array ordenado
        const horarios = Object.keys(horariosAgrupados)
            .sort((a, b) => {
                const [h1, m1] = a.split(':').map(Number);
                const [h2, m2] = b.split(':').map(Number);
                if (h1 !== h2) return h1 - h2;
                return m1 - m2;
            })
            .map(hora => ({
                hora: hora,
                parroquias: horariosAgrupados[hora].map(p => p.nombre),
                parroquias_ids: horariosAgrupados[hora].map(p => p.id)
            }));
        
        res.json({
            fecha: hoy.toISOString(),
            dia_semana: diaSemana,
            horarios: horarios
        });
    } catch (err) {
        console.error('Error:', err);
        res.status(500).json({ error: 'Error al obtener horarios' });
    }
});

// Endpoint para obtener todas las parroquias
app.get('/api/parroquias', (req, res) => {
    try {
        const db = readDB();
        res.json(db.parroquias);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Endpoint para obtener detalles de una parroquia específica
app.get('/api/parroquia/:id', (req, res) => {
    try {
        const db = readDB();
        const parroquia = db.parroquias.find(p => p.id === parseInt(req.params.id));
        
        if (!parroquia) {
            res.status(404).json({ error: 'Parroquia no encontrada' });
            return;
        }
        
        res.json(parroquia);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.listen(PORT, () => {
    console.log(`\n🚀 Servidor corriendo en http://localhost:${PORT}`);
    console.log(`📅 Mostrando horarios para ${new Date().toLocaleDateString('es-ES', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}`);
    console.log(`💾 Usando JSON como almacenamiento\n`);
});
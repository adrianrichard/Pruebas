const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const dbPath = path.join(__dirname, 'misas.db');
const db = new sqlite3.Database(dbPath);

// Crear tablas
db.serialize(() => {
    // Tabla de parroquias
    db.run(`
        CREATE TABLE IF NOT EXISTS parroquias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT
        )
    `);

    // Tabla de horarios de misa
    db.run(`
        CREATE TABLE IF NOT EXISTS horarios_misa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            parroquia_id INTEGER NOT NULL,
            dia_semana INTEGER NOT NULL, -- 0=Domingo, 1=Lunes, ..., 6=Sábado
            hora TIME NOT NULL,
            FOREIGN KEY (parroquia_id) REFERENCES parroquias(id)
        )
    `);

    // Insertar datos de ejemplo
    const insertParroquia = db.prepare(`
        INSERT OR IGNORE INTO parroquias (id, nombre, direccion) 
        VALUES (?, ?, ?)
    `);

    const insertHorario = db.prepare(`
        INSERT OR IGNORE INTO horarios_misa (parroquia_id, dia_semana, hora)
        VALUES (?, ?, ?)
    `);

    // Parroquias de ejemplo
    const parroquiasData = [
        [1, 'Parroquia San Miguel Arcángel', 'Calle Principal 123'],
        [2, 'Nuestra Señora del Rosario', 'Av. Central 456'],
        [3, 'Santa Teresa de Jesús', 'Plaza Mayor 789'],
        [4, 'Catedral Metropolitana', 'Centro Histórico 1'],
        [5, 'Santo Domingo de Guzmán', 'Barrio Norte 234'],
        [6, 'Jesús Obrero', 'Barrio Sur 567'],
        [7, 'San Francisco de Asís', 'Av. Libertador 890'],
        [8, 'Nuestra Señora de Luján', 'Ruta 8 km 45'],
        [9, 'Inmaculada Concepción', 'Calle Iglesia 333'],
        [10, 'San José Obrero', 'Barrio Industrial 777']
    ];

    parroquiasData.forEach(p => {
        insertParroquia.run(p[0], p[1], p[2]);
    });

    // Horarios de ejemplo (día actual = lunes, usamos dia_semana=1 para lunes)
    const horariosData = [
        [1, 1, '09:00'], [1, 1, '10:30'], [1, 1, '12:00'], [1, 1, '18:30'], [1, 1, '20:00'],
        [2, 1, '09:00'], [2, 1, '11:00'], [2, 1, '17:00'], [2, 1, '19:00'], [2, 1, '20:30'],
        [3, 1, '10:00'], [3, 1, '12:00'], [3, 1, '18:00'], [3, 1, '19:30'],
        [4, 1, '09:30'], [4, 1, '11:30'], [4, 1, '17:30'], [4, 1, '19:00'], [4, 1, '20:00'], [4, 1, '21:00'],
        [5, 1, '09:00'], [5, 1, '18:00'], [5, 1, '20:00'],
        [6, 1, '10:30'], [6, 1, '12:30'], [6, 1, '17:00'], [6, 1, '19:30'],
        [7, 1, '09:00'], [7, 1, '11:00'], [7, 1, '18:30'], [7, 1, '20:15'],
        [8, 1, '09:15'], [8, 1, '17:00'], [8, 1, '19:00'], [8, 1, '20:30'],
        [9, 1, '10:00'], [9, 1, '12:00'], [9, 1, '18:00'], [9, 1, '20:00'],
        [10, 1, '09:30'], [10, 1, '11:30'], [10, 1, '17:30'], [10, 1, '19:00'], [10, 1, '21:00']
    ];

    horariosData.forEach(h => {
        insertHorario.run(h[0], h[1], h[2]);
    });

    console.log('Base de datos creada exitosamente');
});

module.exports = db;
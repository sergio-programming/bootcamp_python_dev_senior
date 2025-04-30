CREATE DATABASE IF NOT EXISTS academia;

-- Tabla: Estudiantes
CREATE TABLE estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    correo_electronico varchar(100) unique not null,
    telefono varchar(50)
);

-- Tabla: Profesores
CREATE TABLE profesores (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    correo_electronico varchar(100) unique not null,
    telefono varchar(50),
    especialidad varchar(50)
);

-- Tabla: Cursos
CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) not null,
    descripcion text,
    duracion_horas int,
    profesor_id int,
    foreign key (profesor_id) references Profesores(id_profesor)
        on delete cascade on update cascade
);

-- Tabla: Matriculas(Relacion muchos a muchos(N:N) Entre estudiantes y Cursos)
CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    curso_id INT,
    fecha_matricula DATE,
    FOREIGN KEY (estudiante_id) REFERENCES Estudiantes(id_estudiante)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (curso_id) REFERENCES Cursos(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla: Horarios(Relacion uno a muchos(1:N) Entre Cursos y Horarios)
CREATE TABLE horarios (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    curso_id INT,
    dia_semana VARCHAR(50),
    hora_inicio TIME,
    hora_fin TIME,
    FOREIGN KEY (curso_id) REFERENCES Cursos(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO estudiantes (nombre, apellido, correo_electronico, telefono) VALUES
('Laura', 'Gómez', 'laura.gomez@email.com', '3112345678'),
('Carlos', 'Martínez', 'carlos.martinez@email.com', '3001122334'),
('Ana', 'Ruiz', 'ana.ruiz@email.com', '3123456789'),
('Pedro', 'López', 'pedro.lopez@email.com', '3134567890'),
('Sofía', 'Pérez', 'sofia.perez@email.com', '3145678901'),
('Juan', 'Ramírez', 'juan.ramirez@email.com', '3156789012'),
('Camila', 'Torres', 'camila.torres@email.com', '3167890123'),
('Andrés', 'Moreno', 'andres.moreno@email.com', '3178901234'),
('Mariana', 'Vargas', 'mariana.vargas@email.com', '3189012345'),
('Diego', 'Fernández', 'diego.fernandez@email.com', '3190123456');

INSERT INTO profesores (nombre, apellido, correo_electronico, telefono, especialidad) VALUES
('Luis', 'García', 'luis.garcia@email.com', '3101234567', 'Matemáticas'),
('Elena', 'Navarro', 'elena.navarro@email.com', '3112345678', 'Física'),
('Jorge', 'Castro', 'jorge.castro@email.com', '3123456789', 'Química'),
('Sandra', 'Córdoba', 'sandra.cordoba@email.com', '3134567890', 'Literatura'),
('Raúl', 'Pineda', 'raul.pineda@email.com', '3145678901', 'Historia'),
('Patricia', 'Méndez', 'patricia.mendez@email.com', '3156789012', 'Inglés'),
('Alberto', 'Salazar', 'alberto.salazar@email.com', '3167890123', 'Biología'),
('Lucía', 'Campos', 'lucia.campos@email.com', '3178901234', 'Educación Física'),
('Tomás', 'Reyes', 'tomas.reyes@email.com', '3189012345', 'Informática'),
('Diana', 'Ortiz', 'diana.ortiz@email.com', '3190123456', 'Artes');

SELECT c.id_curso, c.nombre, c.descripcion, c.duracion_horas, c.profesor_id, CONCAT(p.nombre, ' ', p.apellido)
FROM cursos c
JOIN profesores p ON c.profesor_id = p.id_profesor;

SELECT c.id_curso, c.nombre, c.descripcion, c.duracion_horas, c.profesor_id, CONCAT(p.nombre, ' ', p.apellido)
FROM cursos c
JOIN profesores p ON c.profesor_id = p.id_profesor
WHERE c.id_curso = %s;

SELECT m.id_matricula, m.estudiante_id, CONCAT(e.nombre, ' ', e.apellido), m.curso_id, c.nombre, m.fecha_matricula
FROM matriculas m
JOIN estudiantes e ON m.estudiante_id = e.id_estudiante
JOIN cursos c ON m.curso_id = c.id_curso;

SELECT m.id_matricula, m.estudiante_id, CONCAT(e.nombre, ' ', e.apellido), m.curso_id, c.nombre, m.fecha_matricula
FROM matriculas m
JOIN estudiantes e ON m.estudiante_id = e.id_estudiante
JOIN cursos c ON m.curso_id = c.id_curso
WHERE m.id_matricula = %s;

SELECT h.id_horario, h.curso_id, c.nombre, h.dia_semana, h.hora_inicio, h.hora_fin
FROM horarios h
JOIN cursos c ON h.curso_id = c.id_curso;

SELECT h.id_horario, h.curso_id, c.nombre, h.dia_semana, h.hora_inicio, h.hora_fin
FROM horarios h
JOIN cursos c ON h.curso_id = c.id_curso
WHERE h.id_horario = %s;
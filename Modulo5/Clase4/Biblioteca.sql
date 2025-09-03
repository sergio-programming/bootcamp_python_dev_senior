-- Tabla Editorial
CREATE TABLE Editorial(
	id_editorial INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(100),
    anio_fundacion INT
);

-- Tabla Autor
CREATE TABLE Autor(
	id_autor INT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE,
    biografia TEXT
);

-- Tabla Libro (Relacion uno a muchos(1:N))
CREATE TABLE Libro(
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    anio_publicacion INT,
    numero_paginas INT,
    genero VARCHAR(50),
    editorial_id INT,
    FOREIGN KEY (editorial_id) REFERENCES Editorial(id_editorial)
);

-- Table intermedia LibroAutor (Relacion muchos a muchos(N:N))S
CREATE TABLE LibroAutor(
    libro_id INT,
    autor_id INT,
    PRIMARY KEY (libro_id, autor_id),
    FOREIGN KEY (libro_id) REFERENCES Libro(id_libro),
    FOREIGN KEY (autor_id) REFERENCES Autor(id_autor)
);

-- Tabla Usuario
CREATE TABLE Usuario(
    id_usuario INT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT,
    fecha_registro DATETIME DEFAULT current_timestamp
);

-- Tabla prestamo (Relacion uno a muchos(1:N))
CREATE TABLE Prestamo(
    id_prestamo INT PRIMARY KEY,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    estado VARCHAR(20) DEFAULT 'pendiente', -- 'Pendiente', 'Devuelto', 'cancelado'
    usuario_id INT,
    libro_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (libro_id) REFERENCES Libro(id_libro)
);

-- Insert de prueba para todas las tablas

-- Editorial
INSERT INTO Editorial(id_editorial, nombre, pais, anio_fundacion)
VALUES (1, 'Editorial Planeta', 'Espa a', 1949),
       (2, 'Anagrama', 'Espa a', 1969),
       (3, 'Santillana', 'Argentina', 1960);

-- Autor
INSERT INTO Autor(id_autor, nombre_completo, nacionalidad, fecha_nacimiento, biografia)
VALUES (1, 'Gabriel Garcia Marquez', 'Colombia', '1927-03-06', 'Escritor colombiano ganador del Premio Nobel de Literatura en 1982'),
       (2, 'Ernesto Sabato', 'Argentina', '1911-06-24', 'Escritor argentino'),
       (3, 'Julio Cortazar', 'Argentina', '1914-08-26', 'Escritor argentino');

-- Libro
INSERT INTO Libro(id_libro, titulo, isbn, anio_publicacion, numero_paginas, genero, editorial_id)
VALUES (1, 'Cien a os de soledad', '978-607-07-0366-8', 1967, 448, 'Novela', 1),
       (2, 'El tunel', '978-84-339-0416-4', 1959, 272, 'Novela', 2),
       (3, 'Rayuela', '978-950-49-1441-6', 1963, 560, 'Novela', 3);

-- LibroAutor
INSERT INTO LibroAutor(libro_id, autor_id)
VALUES (1, 1),
       (2, 2),
       (3, 3);

-- Usuario
INSERT INTO Usuario(id_usuario, nombre_completo, correo_electronico, telefono, direccion)
VALUES (1, 'Juan Perez', 'jperez@dominio.com', '1234567', 'Calle 1 # 2-3'),
       (2, 'Maria Gomez', 'mgomez@dominio.com', '9876543', 'Calle 2 # 4-5'),
       (3, 'Pedro Lopez', 'plopez@dominio.com', '555-1234', 'Calle 3 # 6-7');

-- Prestamo
INSERT INTO Prestamo(id_prestamo, fecha_prestamo, fecha_devolucion, estado, usuario_id, libro_id)
VALUES (1, '2020-01-01', NULL, 'pendiente', 1, 1),
       (2, '2020-01-15', '2020-01-20', 'devuelto', 2, 2),
       (3, '2020-02-01', NULL, 'cancelado', 3, 3);


-- Consultas entre tablas (JOIN)


select
    P.id_prestamo as id_prestamo,
    U.nombre_completo as nombre_usuario,
    L.titulo as titulo_libro,
    P.fecha_prestamo,
    case
        when P.estado = cancelado then 'Prestamo cancelado'
        when P.fecha_devolucion is null then 'Libro aun no ha sido devuelto'
        else date_format(P.fecha_devolucion, '%Y-%m-%d')
        end as  fecha_devolucion,
        P.estado
from prestamo P
join usuario u on P.usuario_id = U.id_usuario
join libro L on P.libro_id = L.libro_id;

select
    L.titulo as libro,
    A.nombre as autor

from Libro as L
join LibroAutor as LA on L.id_libro = LA.libro_id
join Autor as A on LA.autor_id = A.id_autor
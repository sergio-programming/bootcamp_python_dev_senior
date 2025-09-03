CREATE DATABASE AcademiaDevSenior;
USE AcademiaDevSenior;
CREATE TABLE estudiantes(
	id int primary key auto_increment,
    nombre varchar(100),
    edad int,
    curso_id int,
    foreign key (curso_id) references cursos(id_curso)
);


select *from estudiantes;

create table profesores(
	id_profesor int primary key auto_increment,
    nombre varchar(100),
    especialidad varchar(100),
    experiencia int
);

update estudiantes
set curso = "Java la ruta maestra del codigo" where id=2;

drop table docentes;
drop table estudiantes;

insert into estudiantes (nombre, edad, curso_id) values
("Sergio Pedraza", 36, 2),
("Diana Tovar", 27, 1),
("Andres Ramirez", 19, 2),
("Laura Tegua", 26, 1),
("Maria Cardenas", 23, 2),
("Miguel Avila", 39, 1),
("Laura Perez", 28, 2),
("Diego Perez", 22, 1),
("Jorge Cortes", 30, 2),
("Ingrid Pelaez", 24, 1);

create table cursos (
	id_curso int PRIMARY KEY auto_increment,
    nombre varchar(100),
    profesor_id int,
    foreign key (profesor_id) references profesores(id_profesor)
);

insert into profesores (nombre, especialidad, experiencia) values 
("Johan Gordillo", "Java", 15),
("Juan Triana", "Python", 10);

insert into cursos (nombre, profesor_id) values
("Java la ruta maestra del codigo", 1),
("Python de cero a Senior", 1);

select *from profesores;
select *from cursos;

select estudiantes.nombre as nombre_estudiante, cursos.nombre as nombre_curso
from estudiantes
join cursos on estudiantes.curso_id = cursos.id_curso;
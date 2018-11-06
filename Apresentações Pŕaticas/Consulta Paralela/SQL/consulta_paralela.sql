select * from pg_settings where name like '%parallel%';
set max_parallel_workers_per_gather = 2;
set force_parallel_mode = ON;

EXPLAIN ANALYSE SELECT nom_alu, nom_curso, mgp from alunos inner join cursos on alunos.cod_curso = cursos.cod_curso;

select count(*) from alunos

EXPLAIN ANALYSE SELECT * from alunos
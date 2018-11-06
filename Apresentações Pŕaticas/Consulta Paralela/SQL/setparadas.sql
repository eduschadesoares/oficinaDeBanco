select * from pg_settings where name like '%parallel%';

set max_parallel_workers_per_gather = 2;

set force_parallel_mode = ON;

------

SET parallel_tuple_cost TO DEFAULT;

SET max_parallel_workers_per_gather TO 0;

--------

﻿SET max_parallel_workers_per_gather TO 2;

EXPLAIN ANALYSE select nom_alu,nom_curso from alunos,cursos where alunos.cod_curso = cursos.cod_curso;


--------
Inner

EXPLAIN ANALYSE SELECT nom_alu, nom_curso, mgp from alunos inner join cursos on alunos.cod_curso = cursos.cod_curso;


2 -

SELECT nom_alu, nom_curso, mgp from alunos inner join cursos on alunos.cod_curso = cursos.cod_curso where mgp > 7;

3 - 

SELECT nom_alu, nom_curso, mgp from alunos inner join cursos on alunos.cod_curso = cursos.cod_curso where mgp > 7 and dat_nasc > '01/01/1985';

4 - 

SELECT nom_alu, nom_curso, mgp from alunos inner join cursos on alunos.cod_curso = cursos.cod_curso where mgp > 7 and dat_nasc > '01/01/1985' order by nom_alu ASC;




5 - 

EXPLAIN ANALYSE select nom_alu from alunos where mgp > 7 order by nom_alu ASC;

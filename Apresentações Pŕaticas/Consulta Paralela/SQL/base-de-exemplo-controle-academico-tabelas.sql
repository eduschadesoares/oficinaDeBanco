create table cursos(
    cod_curso    int     not null check( cod_curso > 0 ),
    tot_cred     int     not null check( tot_cred >= 0 ),
    nom_curso    varchar(60)  not null,
    cod_coord    int,
    constraint crs_pk primary key( cod_curso ),
    constraint crs_uk unique( cod_coord ) );

create table professores(
    cod_prof     int     not null check( cod_prof > 0 ),
    cod_curso    int     not null check( cod_curso > 0 ),
    nom_prof     varchar(60)  not null,
    email        varchar(30),
    constraint prf_pk primary key( cod_prof ) );

create table disciplinas(
    cod_disc       int     not null check( cod_disc > 0 ),
    qtd_cred       int     not null check( qtd_cred between 1 and 36 ),
    nom_disc       varchar(60)  not null,
    cod_disc_equiv int,
    constraint dsc_pk primary key( cod_disc ),
    constraint dsc_equiv_fk foreign key ( cod_disc ) references disciplinas (cod_disc) );

create table pre_requisitos(
    cod_disc     int     not null check( cod_disc > 0 ),
    cod_disc_pre int     not null check( cod_disc_pre > 0 ),
    constraint pre_pk primary key( cod_disc, cod_disc_pre ) );

create table curriculos(
    cod_curso    int     not null check( cod_curso > 0 ),
    cod_disc     int     not null check( cod_disc > 0 ),
    periodo      int    not null check( periodo between 1 and 12 ),
    constraint cur_pk primary key( cod_curso, cod_disc ) );

create table alunos(
    mat_alu      int     not null check( mat_alu > 0 ),
    cod_curso    int     not null check( cod_curso > 0 ),
    dat_nasc     date          not null,
    tot_cred     int     not null check( tot_cred >= 0 ),
    mgp          float   not null check( mgp between 0 and 10 ),
    nom_alu      varchar(60)  not null,
    email        varchar(30),
    constraint alu_pk primary key( mat_alu ) );

create table turmas(
    ano          int     not null check( ano > 0 ),
    semestre     int     not null check( semestre in( 1, 2 ) ),
    cod_disc     int     not null check( cod_disc > 0 ),
    turma        char(3)       not null,
    tot_vagas    int     not null check( tot_vagas >= 0 ),
    vag_ocup     int     not null check( vag_ocup >= 0 ),
    cod_prof     int              check( cod_prof > 0 ),
    constraint tur_pk primary key( ano, semestre, cod_disc, turma ) );

create table historicos_escolares(
    ano          int     not null check( ano > 0 ),
    semestre     int     not null check( semestre in( 1, 2 ) ),
    cod_disc     int     not null check( cod_disc > 0 ),
    mat_alu      int     not null check( mat_alu > 0 ),
    media        float   not null check( media between 0 and 10 ),
    faltas       float     not null check( faltas >= 0 ),
    situacao     char(2)       not null check( situacao in ( 'AP', 'RF', 'RM' ) ),
    constraint hst_pk primary key( ano, semestre, cod_disc, mat_alu ) );

create table turmas_matriculadas(
    ano          int     not null check( ano > 0 ),
    semestre     int     not null check( semestre in( 1, 2 ) ),
    cod_disc     int     not null check( cod_disc > 0 ),
    turma        char(3)       not null,
    mat_alu      int     not null check( mat_alu > 0 ),
    nota_1       float            check( nota_1 between 0 and 10 ),
    nota_2       float            check( nota_2 between 0 and 10 ),
    nota_3       float            check( nota_3 between 0 and 10 ),
    nota_4       float            check( nota_4 between 0 and 10 ),
    faltas_1     int              check( faltas_1 >= 0 ),
    faltas_2     int              check( faltas_2 >= 0 ),
    faltas_3     int              check( faltas_3 >= 0 ),
    constraint mat_pk primary key( ano, semestre, cod_disc, mat_alu ) );
create table conceitos(
    conceito     char(1) not null constraint con_pk primary key check ( conceito in ( 'A','B','C','D','E' ) ),
    faixa_ini    float not null check (faixa_ini >= 0),
    faixa_fim    float not null check (faixa_fim >= 0) );







alter table cursos add constraint crs_prf_fk foreign key( cod_coord ) references professores( cod_prof );
alter table professores add constraint prf_crs_fk foreign key( cod_curso ) references cursos( cod_curso );
alter table pre_requisitos add constraint pre_dsc_fk foreign key( cod_disc ) references disciplinas( cod_disc );
alter table pre_requisitos add constraint pre_dsc_pre_fk foreign key( cod_disc_pre ) references disciplinas( cod_disc );
alter table curriculos add constraint cur_crs_fk foreign key( cod_curso ) references cursos( cod_curso );
alter table curriculos add constraint cur_dsc_fk foreign key( cod_disc ) references disciplinas( cod_disc );
alter table alunos add constraint alu_crs_fk foreign key( cod_curso ) references cursos( cod_curso );
alter table turmas add constraint tur_dsc_fk foreign key( cod_disc ) references disciplinas( cod_disc );
alter table turmas add constraint tur_prf_fk foreign key( cod_prof ) references professores( cod_prof );
alter table historicos_escolares add constraint hst_dsc_fk foreign key( cod_disc ) references disciplinas( cod_disc );
alter table historicos_escolares add constraint hst_alu_fk foreign key( mat_alu ) references alunos( mat_alu );
alter table turmas_matriculadas add constraint mat_tur_fk foreign key( ano, semestre, cod_disc, turma ) references turmas( ano, semestre, cod_disc, turma );
alter table turmas_matriculadas add constraint mat_alu_fk foreign key( mat_alu ) references alunos( mat_alu );





create index crs_nom_i on cursos( nom_curso );
create index prf_crs_i on professores( cod_curso );
create index prf_nom_i on professores( nom_prof );
create index dsc_nom_i on disciplinas( nom_disc );
create index pre_dsc_i on pre_requisitos( cod_disc );
create index pre_dsc_pre_i on pre_requisitos( cod_disc_pre );
create index cur_crs_i on curriculos( cod_curso );
create index cur_dsc_i on curriculos( cod_disc );
create index alu_nom_i on alunos( nom_alu );
create index tur_dsc_i on turmas( cod_disc );
create index tur_prf_i on turmas( cod_prof );
create index hst_dsc_i on historicos_escolares( cod_disc );
create index hst_alu_i on historicos_escolares( mat_alu );
create index mat_alu_i on turmas_matriculadas( mat_alu );
create index mat_tur_i on turmas_matriculadas( ano, semestre, cod_disc, turma );
create index cod_disc_equiv_i on disciplinas( cod_disc_equiv );

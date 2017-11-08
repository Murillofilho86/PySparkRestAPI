create database spark_api;

use spark_api;

create table step(
	id int not null,
    name varchar(155),
    description varchar(155),
    constraint pk_step primary key (id)
);

insert into step values (1, 'START', 'Geração do token para identificação da história do workflow do processo')
insert into step values (2, 'LOAD', 'Definição da url da fonte de dados e tipo do arquivo a ser importado')

create table process(
	id int not null auto_increment,
    step_id int not null,
    token varchar(100) not null,
    data varchar(21844) not null,
    date datetime not null,
    constraint pk_process primary key (id),
    constraint fk_step foreign key (step_id) references step (id),
    constraint uc_process_step_token unique(step_id, token)
);

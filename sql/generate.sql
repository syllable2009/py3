create table special_voa
(
    id          bigint auto_increment
        comment '无业务含义',
    cat_cn      varchar(255)                       null
        comment '中文分类',
    cat_en      varchar(255)                       null
        comment '英文分类',
    title       varchar(255)                       null
        comment '标题',
    content     text                               null
        comment '内容',
    create_time datetime default CURRENT_TIMESTAMP null
        comment '创建时间',
    update_time datetime default CURRENT_TIMESTAMP null
        on update CURRENT_TIMESTAMP
        comment '最后更新时间',
    href        varchar(255)                       null,
    date        date                               null,
    constraint special_voa_title_cat_cn_uindex
        unique (title, cat_cn)
)
    ENGINE = InnoDB
    DEFAULT CHARSET = utf8mb4
    DEFAULT COLLATE = utf8mb4_unicode_ci;


create table user
(
    aid         bigint(20) unsigned auto_increment comment '自增主键' primary key,
    uid         varchar(36)                        not null COMMENT 'uuid',
    user_name   varchar(36)                        not null COMMENT '用户id',
    user_age    int(11)  default null COMMENT '用户年龄',
    create_time datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_time datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    constraint idx_uid unique (uid)
) comment '关注表' default charset = utf8mb4
                   COLLATE = utf8mb4_unicode_ci
                   engine = InnoDB;
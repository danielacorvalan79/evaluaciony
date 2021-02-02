PGDMP     9    7                y           meds    12.5    12.5                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                        0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            !           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            "           1262    32876    meds    DATABASE     �   CREATE DATABASE meds WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Chile.1252' LC_CTYPE = 'Spanish_Chile.1252';
    DROP DATABASE meds;
                postgres    false            �            1259    16439 
   asignatura    TABLE     �   CREATE TABLE public.asignatura (
    asignatura_id bigint NOT NULL,
    departamento_id bigint NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion character varying(1000)
);
    DROP TABLE public.asignatura;
       public         heap    postgres    false            �            1259    16435    asignatura_asignatura_id_seq    SEQUENCE     �   CREATE SEQUENCE public.asignatura_asignatura_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.asignatura_asignatura_id_seq;
       public          postgres    false    208            #           0    0    asignatura_asignatura_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.asignatura_asignatura_id_seq OWNED BY public.asignatura.asignatura_id;
          public          postgres    false    206            �            1259    16437    asignatura_departamento_id_seq    SEQUENCE     �   CREATE SEQUENCE public.asignatura_departamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.asignatura_departamento_id_seq;
       public          postgres    false    208            $           0    0    asignatura_departamento_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.asignatura_departamento_id_seq OWNED BY public.asignatura.departamento_id;
          public          postgres    false    207            �            1259    16415    profesor    TABLE     �   CREATE TABLE public.profesor (
    id bigint NOT NULL,
    nombre character varying(25),
    apellido character varying(50),
    escuela character varying(50),
    fecha_de_contratacion date,
    sueldo numeric
);
    DROP TABLE public.profesor;
       public         heap    postgres    false            �            1259    16426 
   profesores    TABLE     �   CREATE TABLE public.profesores (
    id bigint NOT NULL,
    nombre character varying(25) NOT NULL,
    apellido character varying(50),
    escuela character varying(50),
    fecha_de_contratacion date,
    sueldo numeric
);
    DROP TABLE public.profesores;
       public         heap    postgres    false            �            1259    16413    profesores_id_seq    SEQUENCE     z   CREATE SEQUENCE public.profesores_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.profesores_id_seq;
       public          postgres    false    203            %           0    0    profesores_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.profesores_id_seq OWNED BY public.profesor.id;
          public          postgres    false    202            �            1259    16424    profesores_id_seq1    SEQUENCE     {   CREATE SEQUENCE public.profesores_id_seq1
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.profesores_id_seq1;
       public          postgres    false    205            &           0    0    profesores_id_seq1    SEQUENCE OWNED BY     H   ALTER SEQUENCE public.profesores_id_seq1 OWNED BY public.profesores.id;
          public          postgres    false    204            �
           2604    16442    asignatura asignatura_id    DEFAULT     �   ALTER TABLE ONLY public.asignatura ALTER COLUMN asignatura_id SET DEFAULT nextval('public.asignatura_asignatura_id_seq'::regclass);
 G   ALTER TABLE public.asignatura ALTER COLUMN asignatura_id DROP DEFAULT;
       public          postgres    false    206    208    208            �
           2604    16443    asignatura departamento_id    DEFAULT     �   ALTER TABLE ONLY public.asignatura ALTER COLUMN departamento_id SET DEFAULT nextval('public.asignatura_departamento_id_seq'::regclass);
 I   ALTER TABLE public.asignatura ALTER COLUMN departamento_id DROP DEFAULT;
       public          postgres    false    207    208    208            �
           2604    16418    profesor id    DEFAULT     l   ALTER TABLE ONLY public.profesor ALTER COLUMN id SET DEFAULT nextval('public.profesores_id_seq'::regclass);
 :   ALTER TABLE public.profesor ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            �
           2604    16429    profesores id    DEFAULT     o   ALTER TABLE ONLY public.profesores ALTER COLUMN id SET DEFAULT nextval('public.profesores_id_seq1'::regclass);
 <   ALTER TABLE public.profesores ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205                      0    16439 
   asignatura 
   TABLE DATA           Y   COPY public.asignatura (asignatura_id, departamento_id, nombre, descripcion) FROM stdin;
    public          postgres    false    208   �                 0    16415    profesor 
   TABLE DATA           `   COPY public.profesor (id, nombre, apellido, escuela, fecha_de_contratacion, sueldo) FROM stdin;
    public          postgres    false    203   �                 0    16426 
   profesores 
   TABLE DATA           b   COPY public.profesores (id, nombre, apellido, escuela, fecha_de_contratacion, sueldo) FROM stdin;
    public          postgres    false    205   Z       '           0    0    asignatura_asignatura_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.asignatura_asignatura_id_seq', 1, false);
          public          postgres    false    206            (           0    0    asignatura_departamento_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.asignatura_departamento_id_seq', 1, false);
          public          postgres    false    207            )           0    0    profesores_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.profesores_id_seq', 1, true);
          public          postgres    false    202            *           0    0    profesores_id_seq1    SEQUENCE SET     @   SELECT pg_catalog.setval('public.profesores_id_seq1', 7, true);
          public          postgres    false    204            �
           2606    16448    asignatura asignatura_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT asignatura_pkey PRIMARY KEY (asignatura_id);
 D   ALTER TABLE ONLY public.asignatura DROP CONSTRAINT asignatura_pkey;
       public            postgres    false    208            �
           2606    16434    profesores profesores_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.profesores
    ADD CONSTRAINT profesores_pkey PRIMARY KEY (nombre);
 D   ALTER TABLE ONLY public.profesores DROP CONSTRAINT profesores_pkey;
       public            postgres    false    205                  x������ � �         N   x�3�tN,-���L>� �.)��I��N�+�LL�WHIU�ITH�()J�ML)-J�4200�54�52�4� ��b���� ��&           x�M�MN�0�דS�Fv~�d�V���j%ذ�8�v���#���Qz2�DB������a�񀰧@Wx�60Y;�-�Jk��,�E���rX�h��@}l-{�G�Al��t�RU2�aY����b��m)��v��t�p�S���;C�a�4���J��L���Z����E���bU����1`���#��u<�T�z�q�#��p��?M*���a[
l��>$< ���ŪM��Y���V�;=�XV	\w�i�#���4�Ӓ�5z�.��8c�q�Q�z�e�/��n      
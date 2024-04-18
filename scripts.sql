CREATE TABLE IF NOT EXISTS public.rmt_job_listings
(
    id_remotive integer NOT NULL DEFAULT nextval('rmt_job_listings_id_remotive_seq'::regclass),
    url character varying(255) COLLATE pg_catalog."default",
    title character varying(255) COLLATE pg_catalog."default",
    company_name character varying(255) COLLATE pg_catalog."default",
    company_logo character varying(255) COLLATE pg_catalog."default",
    category character varying(100) COLLATE pg_catalog."default",
    job_type character varying(50) COLLATE pg_catalog."default",
    publication_date timestamp without time zone,
    candidate_required_location character varying(150) COLLATE pg_catalog."default",
    salary character varying(255) COLLATE pg_catalog."default",
    description xml,
    collection_date timestamp without time zone,
    job_counting bigint,
    CONSTRAINT rmt_job_listings_pkey PRIMARY KEY (id_remotive)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.rmt_job_listings
    OWNER to remotive_usr;
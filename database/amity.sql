-- how can I run this in python?

DROP DATABASE IF EXISTS amity;

CREATE DATABASE amity;

\c amity;

CREATE TABLE people = (
  email text PRIMARY KEY,
  name text,
  gender text,
  role text,
--   should the stuff that doesn't apply to all people be in a different table?
  title text,
  department text,
  wants_residence text
);

CREATE TABLE rooms = (
  id serial PRIMARY KEY,
  name text,
  occupancy int,
  purpose text
);
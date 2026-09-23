-- La table du compteur d'audience.
--
--   wrangler d1 execute boussole --remote --file=schema.sql
--
-- Quatre colonnes, et rien de plus : un jour, un nom d'événement, l'adresse d'une
-- page du guide le cas échéant, et un nombre. Aucune colonne ne peut désigner une
-- personne — il n'y a ni adresse IP, ni identifiant de visite, ni horodatage à la
-- seconde, qui permettrait de recouper deux événements entre eux.
--
-- La clé primaire porte sur les trois premières colonnes : une seule ligne par
-- jour et par événement, qu'on incrémente. La base reste minuscule — de l'ordre
-- de sept lignes par jour, quelques milliers par an.

CREATE TABLE IF NOT EXISTS compteur (
  jour      TEXT    NOT NULL,           -- AAAA-MM-JJ
  evenement TEXT    NOT NULL,           -- accueil · article · test-debut · test-fin · paywall · stripe
  page      TEXT    NOT NULL DEFAULT '',-- /guide/xxx.html, vide pour les autres événements
  n         INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (jour, evenement, page)
);

-- Les lectures se font toujours sur une plage de dates, jamais sur la table entière.
CREATE INDEX IF NOT EXISTS compteur_jour ON compteur (jour);

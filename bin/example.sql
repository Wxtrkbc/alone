BEGIN;

INSERT INTO "public"."app_user" VALUES ('pbkdf2_sha256$36000$BV750HpxfA5K$4gP6u93Hla29geqsQAAQl7rbysX1yhHvsrUgTTOlQg0=', '2018-02-23 07:53:45.79801+00', '2018-01-24 08:28:46.385833+00', '2018-01-24 08:28:46.385895+00', '2950d500-3609-4254-8538-2192b0a9f610', 'ahprosim', '', '', 'static/ins/ahprosim.jpg', '{}', 'MALE', '', 'NORMAL', 'f');
INSERT INTO "public"."app_user" VALUES ('pbkdf2_sha256$36000$BV750HpxfA5K$4gP6u93Hla29geqsQAAQl7rbysX1yhHvsrUgTTOlQg0=', '2018-02-23 07:53:45.79801+00', '2018-01-24 08:28:46.385833+00', '2018-01-24 08:28:46.385895+00', '2950d500-3609-4254-8538-2192b0a9f611', 'steveaoki', '', '', 'static/ins/steveaoki.jpg', '{}', 'MALE', '', 'NORMAL', 'f');
INSERT INTO "public"."app_user" VALUES ('pbkdf2_sha256$36000$BV750HpxfA5K$4gP6u93Hla29geqsQAAQl7rbysX1yhHvsrUgTTOlQg0=', '2018-02-23 07:53:45.79801+00', '2018-01-24 08:28:46.385833+00', '2018-01-24 08:28:46.385895+00', '2950d500-3609-4254-8538-2192b0a9f612', 'liuwenlw', '', '', 'static/ins/liuwenlw.jpg', '{}', 'FEMALE', '', 'NORMAL', 'f');
INSERT INTO "public"."app_user" VALUES ('pbkdf2_sha256$36000$BV750HpxfA5K$4gP6u93Hla29geqsQAAQl7rbysX1yhHvsrUgTTOlQg0=', '2018-02-23 07:53:45.79801+00', '2018-01-24 08:28:46.385833+00', '2018-01-24 08:28:46.385895+00', '2950d500-3609-4254-8538-2192b0a9f613', 'dualipa', '', '', 'static/ins/dualipa.jpg', '{}', 'FEMALE', '', 'NORMAL', 'f');
INSERT INTO "public"."app_user" VALUES ('pbkdf2_sha256$36000$BV750HpxfA5K$4gP6u93Hla29geqsQAAQl7rbysX1yhHvsrUgTTOlQg0=', '2018-02-23 07:53:45.79801+00', '2018-01-24 08:28:46.385833+00', '2018-01-24 08:28:46.385895+00', '2950d500-3609-4254-8538-2192b0a9f614', 'natgeo', '', '', 'static/ins/natgeo.jpg', '{}', 'UNDEFINED', '', 'NORMAL', 'f');
INSERT INTO "public"."app_user" VALUES ('pbkdf2_sha256$36000$BV750HpxfA5K$4gP6u93Hla29geqsQAAQl7rbysX1yhHvsrUgTTOlQg0=', '2018-02-23 07:53:45.79801+00', '2018-01-24 08:28:46.385833+00', '2018-01-24 08:28:46.385895+00', '2950d500-3609-4254-8538-2192b0a9f615', 'angelinajolieofficial', '', '', 'static/ins/angelinajolieofficial.jpg', '{}', 'UNDEFINED', '', 'NORMAL', 'f');


INSERT INTO "public"."app_ins" VALUES ('2018-01-24 09:06:10.434257+00', '2018-01-24 09:06:10.434342+00', '3a3538d9-1a29-45c1-9d71-f3e65c988b66', 'Amazing night', 'PICTURE-INS', '["static/ins/steve1-1.jpg"]', '2950d500-3609-4254-8538-2192b0a9f611');
INSERT INTO "public"."app_ins" VALUES ('2018-01-24 09:06:10.434257+00', '2018-01-24 09:06:10.434342+00', '3a3538d9-1a29-45c1-9d71-f3e65c988b67', 'Thank you so much for having me team ', 'PICTURE-INS', '["static/ins/liuwenlw1-1.jpg"]', '2950d500-3609-4254-8538-2192b0a9f612');
INSERT INTO "public"."app_ins" VALUES ('2018-01-24 09:06:10.434257+00', '2018-01-24 09:06:10.434342+00', '3a3538d9-1a29-45c1-9d71-f3e65c988b68', 'My head still hurts', 'PICTURE-INS', '["static/ins/dualipa1-1.jpg"]', '2950d500-3609-4254-8538-2192b0a9f612');
INSERT INTO "public"."app_ins" VALUES ('2018-01-24 09:06:10.434257+00', '2018-01-24 09:06:10.434342+00', '3a3538d9-1a29-45c1-9d71-f3e65c988b69', 'A man shows off his mother', 'PICTURE-INS', '["static/ins/natgeo1-1.jpg"]', '2950d500-3609-4254-8538-2192b0a9f612');

INSERT INTO "public"."app_user_followed" VALUES ('1', '2950d500-3609-4254-8538-2192b0a9f610', '2950d500-3609-4254-8538-2192b0a9f611');
INSERT INTO "public"."app_user_followed" VALUES ('5', '2950d500-3609-4254-8538-2192b0a9f610', '2950d500-3609-4254-8538-2192b0a9f612');
INSERT INTO "public"."app_user_followed" VALUES ('6', '2950d500-3609-4254-8538-2192b0a9f610', '2950d500-3609-4254-8538-2192b0a9f613');
INSERT INTO "public"."app_user_followed" VALUES ('7', '2950d500-3609-4254-8538-2192b0a9f610', '2950d500-3609-4254-8538-2192b0a9f614');
INSERT INTO "public"."app_user_followed" VALUES ('8', '2950d500-3609-4254-8538-2192b0a9f610', '2950d500-3609-4254-8538-2192b0a9f615');

COMMIT;
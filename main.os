push prtext, >Welcome to a random code made in osani lang<

define int> n1, 10
define string> msg, >Hello good world!<
define bool> isTrue, true
define float> n2, 10.50

define function, welcome

add funccode, welcome @> push prtext, >Welcome to osanilang< @<

push newline

call, welcome

push prvar, >nothing<

push newline
push prvar, >n1<
push newline
push prvar, >msg<
push newline
push prvar, >isTrue<
push newline
push prvar, >n2<

add oscmd, hello

add oscode, hello @> push prtext, >hello!< @<
add oscode, hello @> push newline @<

add oscmd, talk

add oscode, talk @> define input, msg @>say something > @<
add oscode, talk @> push prvar, >msg< @<
add oscode, talk @> push newline @<

add cmd, randnum

add code, randnum @> from random import randint @<
add code, randnum @> print(randint(1,10)) @<

push newline

start osanilang

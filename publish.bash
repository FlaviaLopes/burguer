now="$(date +'%d/%m/%Y %Hh %mm %Ss')"
rm -rf deploy
mkdir deploy
pelican -o deploy -s publishconf.py
css-html-js-minify deploy
git checkout -b gh-pages --track destiny/master
ghp-import deploy -b gh-pages -m "Publicado em $now"
git push git@github.com:FlaviaLopes/burguer.github.io.git gh-pages:master





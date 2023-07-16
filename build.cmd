python builddate.py 
cd site
mkdocs build -d ..\docs -c
cd..
git add *.*
git commit -m .
git push
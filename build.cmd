python builddate.py 
cd site
mkdocs build -d ..\docs -c
cd..
copy CNAME docs
git add *.*
git commit -m .
git push
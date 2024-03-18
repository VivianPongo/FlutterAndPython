link a calculadora desplegada en vercel https://calculadora-gt4jwj7sh-vivs-projects.vercel.app/

primero se crea la app: flet create myapp ///u otro nombre a parte de myapp como ProyectoChatIA o no c xd
se instala flet : pip install flet
mini tuto para deploy
ir a la carpeta y colocar el parche para html (sino no se deploya y sale error 404):   flet publish archivoconcode.py --web-renderer html --route-url-strategy hash
con esto se crea la carpeta dist que subiremos a vercel
instalar vercel ---> https://www.npmjs.com/package/vercel
abrir vercel en la consola en la direccion de la carpeta de la aplicacion en este caso myapp: vercel + enter



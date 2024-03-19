import subprocess

dir = "/Users/rlizardo/Desktop/forza-L17/pbr"
sbs = "/Applications/Substance Painter.app/Contents/MacOS/Substance Painter"
mesh = "--mesh=/Users/rlizardo/Desktop/forza-L17/sf.obj"
#ao = "--mesh-map /Users/rlizardo/Desktop/forza-L17/pbr/sf_material_6_normal_version001.png"
basecolor = "--mesh-map=/Users/rlizardo/Desktop/demo_1/Demo_basecolor.png"
export = "--export-path=/Users/rlizardo/Desktop"
exec = sbs, mesh, basecolor, export
subprocess.call(exec)
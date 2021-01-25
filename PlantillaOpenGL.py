from OpenGL.GL import *
from glew_wish import *
import glfw 
import time

def dibujarTriangulos():
    #rutinas de dibujo
    glBegin(GL_TRIANGLES)
    glColor3f(1,1,0)    
    glVertex3f(-0.5,-0.25,0)    
    glColor3f(1,1,1)    
    glVertex3f(0,0.5,0)    
    #glColor3f(0,0,1)    
    glVertex3f(0.5,-0.25,0)

    glColor3f(0,0,0)
    glVertex3f(-0.25,0.12,0)  
    glVertex3f(0,-0.25,0)  
    glVertex3f(0.25,0.12,0) 
    
    glEnd()

def dibujarLineas():
    #rutinas de dibujo
    glBegin(GL_LINES)
    glColor3f(1,1,0)    
    glVertex3f(-0.5,-0.25,0)       
    glVertex3f(0,0.5,0) 

    glVertex3f(0,0.5,0)  
    glVertex3f(0.5,-0.25,0)

    glVertex3f(0.5,-0.25,0)
    glVertex3f(-0.5,-0.25,0)
    
    glEnd()

def dibujarLineasContinuas():
    #rutinas de dibujo
    glBegin(GL_LINE_STRIP)
    glColor3f(1,1,0)    
    glVertex3f(-0.5,-0.25,0)       
    glVertex3f(-0.5,0.5,0) 

    glVertex3f(0,0.5,0)  
    glVertex3f(0.5,-0.25,0)

    glEnd()

def dibujarLineasLoop():
    #rutinas de dibujo
    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,0)    
    glVertex3f(-0.5,-0.25,0)       
    glVertex3f(-0.5,0.5,0) 

    glVertex3f(0,0.5,0)  
    glVertex3f(0.5,-0.25,0)

    glEnd()

def dibujarPuntos():
    #rutinas de dibujo
    glBegin(GL_POINTS)
    glColor3f(1,1,0)    
    glVertex3f(-0.5,-0.25,0)        
    glVertex3f(0,0.5,0)
    glVertex3f(0.5,-0.25,0)
    
    glEnd()

def dibujarPoligono():
    #rutinas de dibujo
    glBegin(GL_POLYGON)
    glColor3f(1,1,0)    
    glVertex3f(-0.5,-0.25,0)        
    glVertex3f(0,0.5,0)
    glVertex3f(0.5,-0.25,0)
    glVertex3f(0,-1,0)
    
    glEnd()

def dibujarRectangulos():
    #rutinas de dibujo
    glBegin(GL_QUADS)
    glColor3f(1,1,0)    
    glVertex3f(-0.5,-0.25,0)        
    glVertex3f(0,0.5,0)
    glVertex3f(0.5,-0.25,0)
    glVertex3f(1.5,-2.25,0)
    
    glEnd()

def dibujar():
    dibujarTriangulos()
    #dibujarPuntos()
    #dibujarLineas()
    #dibujarLineasContinuas()
    #dibujarLineasLoop()
    #dibujarRectangulos()
    #dibujarPoligono()

def main():
    #inicia glfw
    ancho = 800
    alto = 800
    if not glfw.init():
        return
    #crea la ventana
    #indepentientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"mi ventana",None,None)

    #configuracion open GL
    glfw.window_hint(glfw.SAMPLES,4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return

    #Establecemos el contexto
    glfw.make_context_current(window)

    #activamos la validacion de funcion modernas de OpenGL
    glewExperimental = True

    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return
    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)
    red = 0

    
    while not glfw.window_should_close(window):

        while (red < 1):
            red = red + 0.1
            
            time.sleep(0.1)
            print(red)
            
            #Establece region de dibujo
            glViewport(0,0,ancho,alto)
            #establece color de borrado
            glClearColor(red,0.1,0.8,1)
            #Borra el contenido de la ventana
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            #Dibujar
            dibujar()
            #Preguntar si hubo entrada de periferico
            glfw.poll_events()
            #Intercambia los buffers
            glfw.swap_buffers(window)

            if red > 1:
                 while (red > 0):
                    red = red - 0.1
                    time.sleep(0.1)
                    print(red)
                    
                    #Establece region de dibujo
                    glViewport(0,0,ancho,alto)
                    #establece color de borrado
                    glClearColor(red,0.1,0.8,1)
                    #Borra el contenido de la ventana
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

                    #Dibujar
                    dibujar()
                    #Preguntar si hubo entrada de periferico
                    glfw.poll_events()
                    #Intercambia los buffers
                    glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()
import clases

persona = clases.Persona()
persona.setNombre("Cristian")
persona.setApellidos("Gonzalez")
persona.setAltura("175cm")
persona.setEdad("23 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())


informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")


print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.lenguajes)
print(informatico.caminar())
print(informatico.experiencia)


print("-----------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Cristian Steven")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())

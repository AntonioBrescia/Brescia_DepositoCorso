# In python un modulo è un file, 
# 1 eseguire una singola operazione
# 2 posso essere microparti di unità modulari 
# E' possible importare un modulo tramite import()

import mio_modulo as modulo
modulo.saluta("Antonio")

raggio = 2
cerchio = modulo.Cerchio(raggio)
print(cerchio.area())
# TeNPy: MPS semplice e osservabili locali su una catena di spin-1/2
from tenpy.networks.site import SpinHalfSite
from tenpy.networks.mps import MPS

L = 6
site = SpinHalfSite(conserve=None)              # spin-1/2 senza simmetrie
product_state = ['up'] * L                      # stato prodotto |↑↑...↑>
psi = MPS.from_product_state([site]*L, product_state, bc='finite')

# aspettazione di Sz su ogni sito (array di lunghezza L)
sz = psi.expectation_value('Sz')
print("⟨Sz⟩ per sito:", sz)
print("Lunghezza catena:", psi.L)
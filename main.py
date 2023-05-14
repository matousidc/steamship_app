from steamship import Steamship

# api_key="AB14DB2B-15A2-44B2-BB20-A351F8B7B1B5"
# Load the package instance stub.
pkg = Steamship.use("initial-tst", instance_handle="initial-tst-87d")

name = "bob"
trait = "autistic"
prompt = ""
# Invoke the method
resp = pkg.invoke("generate", name=name, trait=trait)
resp2 = pkg.invoke("generate_ericsson", _prompt=prompt)
print(resp)

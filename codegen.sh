openapi-generator generate \
  -i https://raw.githubusercontent.com/Mykrobe-tools/mykrobe-atlas-tracking-api/master/swagger.yaml \
  -g python \
  -c codegen_configuration.yaml \
  -o .

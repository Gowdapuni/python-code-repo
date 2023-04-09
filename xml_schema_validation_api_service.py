import xml.etree.ElementTree as ET 
from lxml import etree
from flask import Flask, request, jsonify
import xmlschema
from xmlschema import XMLSchemaValidationError


app = Flask(__name__)

@app.route('/schema_validate', methods = ['POST','GET'])
def schema_validate():
    post_man_api_request  = request.data
    root = etree.fromstring(post_man_api_request)

    try:
        xmlschema.validate(root,'schema_food.xsd')
        xml_data = ET.tostring(root, encoding='utf8',method='xml')
        return xml_data,200,{'content-type':'application/xml'}
    
    except XMLSchemaValidationError as e:
        return jsonify({'error': e.message})

if __name__ == "__main__":
    app.run()
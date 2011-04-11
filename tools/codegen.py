#!/usr/bin/env python
"""Generates the amqp.py file used as a foundation for AMQP communication

For copyright and licensing please refer to COPYING.
"""
__author__ = 'Gavin M. Roy'
__email__ = 'gmr@myyearbook.com'
__date__ = '2011-03-31'

CODEGEN_DIR = 'rabbitmq-codegen-default'
CODEGEN_IGNORE_CLASSES = ['access']
CODEGEN_JSON = 'amqp-rabbitmq-0.9.1.json'
CODEGEN_OUTPUT = '../pika/amqp.py'
CODEGEN_URL = 'http://hg.rabbitmq.com/rabbitmq-codegen/archive/default.tar.bz2'

RESERVED_WORDS = 'global'

from datetime import date
from json import load
from os import unlink
from os.path import exists
from re import sub
from tarfile import open as tarfile_open
from tempfile import NamedTemporaryFile
from urllib import urlopen

# Outut buffer list
output = []


def newline(text='', lpad=0):
    """Append a new line to the output buffer"""
    global output

    # If we specified a pad amount
    if lpad:
        # Pad the left of the string
        output.append("%s%s" % (''.join([' ' for position in xrange(0, lpad)]),
                                text))
    # Otherwise just append the string
    else:
        output.append(text)

def classify(text):
    """Replace the AMQP constant with a more pythonic classname"""
    parts = text.split('-')
    class_name = ''
    for part in parts:
        class_name += part.title()
    return class_name


def comment(text):
    """Append a comment to the output buffer"""
    newline('# %s' % text)


def dashify(text):
    """Replace a - with a _ for the passed in text"""
    return text.replace('-', '_')


def indent_and_wrap(text, indent, indent_first_line=False):
    docstring = list()
    padding = ''.join([' ' for position in xrange(0, indent)])
    max_length = 79 - indent
    try:
        offset = text.rindex(' ', 0, max_length)
    except ValueError:
        if indent_first_line:
            return padding + text
        else:
            return text

    if indent_first_line:
        docstring.append(padding + text[0:offset])
    else:
        docstring.append(text[0:offset])
    while (offset + max_length) < len(text):
        try:
            end = text.rindex(' ', offset, offset + max_length)
        except ValueError:
            break
        docstring.append(padding + text[offset:end])
        offset = end
    if offset < len(text):
        docstring.append(padding + text[offset:])
    return '\n'.join(docstring)


def docify(text, indent=4):
    """Return a wrapping docstring block for the given string"""
    docstring = list()
    padding = ''.join([' ' for position in xrange(0, indent)])
    max_length = 79 - indent
    try:
        offset = text.rindex(' ', 0, max_length - 3)
    except ValueError:
        return '%s"""%s"""' % (padding, text)
    docstring.append('%s"""%s' % (padding, text[0:offset]))
    while (offset + max_length) < len(text):
        try:
            end = text.rindex(' ', offset, offset + max_length)
        except ValueError:
            break
        docstring.append(padding + text[offset:end])
        offset = end
    if offset < len(text):
        docstring.append(padding + text[offset:])
    return '\n'.join(docstring) + '\n\n' + padding + '"""'


# Check to see if we have the codegen file in this directory
if not exists(CODEGEN_JSON):

    # Retieve the codegen archive
    print "Downloading codegen JSON file."
    handle = urlopen(CODEGEN_URL)
    bzip2_tarball = handle.read()

    # Write the file out to a temp file
    tempfile = NamedTemporaryFile(delete=False)
    tempfile.write(bzip2_tarball)
    tempfile.close()

    # Extract the CODEGEN_JSON file to this directory
    tarball = tarfile_open(tempfile.name, 'r:*')
    json_data = tarball.extractfile('%s/%s' % (CODEGEN_DIR, CODEGEN_JSON))

    # Write out the JSON file
    with open(CODEGEN_JSON, 'w') as handle:
        handle.write(json_data.read())

    # Remove the tempfile
    unlink(tempfile.name)

# Read in the codegen JSON file
with open(CODEGEN_JSON, 'r') as handle:
    amqp = load(handle)

# Our output list
output = list()

# Create and append our docblock
docblock = '''"""%s

Auto-generated AMQP Support Module

WARNING: DO NOT EDIT. To Generate run tools/codegen.py

For copyright and licensing please refer to COPYING.

"""''' % CODEGEN_OUTPUT.split('/')[-1]
newline(docblock)
newline()

# Append our metadata
newline('__date__ = "%s"' % date.today().isoformat())
newline('__author__ = "%s"' % __file__)
newline()

# AMQP Version Header
comment("AMQP Protocol Version")
newline('AMQP_VERSION = (%i, %i, %i)' % (amqp['major-version'],
                                         amqp['minor-version'],
                                         amqp['revision']))
newline()

# Defaults
comment("RabbitMQ Defaults")
newline('DEFAULT_HOST = "localhost"')
newline('DEFAULT_PORT = %i' % amqp['port'])
newline('DEFAULT_USER = "guest"')
newline('DEFAULT_PASS = "guest"')
newline()

# Constant
comment("AMQP Constants")
for constant in amqp['constants']:
    if 'class' not in constant:
        newline('AMQP_%s = %i' % \
                (dashify(constant['name']), constant['value']))
newline()
newline()

# Warnings and Exceptions
comment("AMQP Errors")
newline()
errors = {}
for constant in amqp['constants']:
    if 'class' in constant:
        class_name = 'AMQP' + classify(constant['name'])
        if constant['class'] == 'soft-error':
            extends = 'Warning'
        elif constant['class'] == 'hard-error':
            extends = 'Exception'
        else:
            raise ValueError('Unexpected class: %s', constant['class'])
        newline('class %s(%s):' % (class_name, extends))
        newline('    """Class used to map AMQP error values to an Exception')
        newline('    or Warning class based upon being a hard or soft error.')
        newline()
        newline('    """')
        newline('    name = "%s"' % constant['name'])
        newline('    value = %i' % constant['value'])
        newline()
        newline()
        errors[constant['value']] = class_name

# Class mapping to id
class_lines = []
for amqp_class in amqp['classes']:
    class_lines.append('                "%s": %i,' % \
                       (amqp_class['name'].upper(), amqp_class['id']))
comment("AMQP class to id mapping")
class_lines[0] = class_lines[0].replace('                ',
                                        'AMQP_CLASSES = {')
class_lines[-1] = class_lines[-1].replace(',', '}')
output += class_lines
newline()

# Error mapping to class
error_lines = []
for error_code in errors.keys():
    error_lines.append('               %i: %s,' % (error_code,
                                                   errors[error_code]))
comment("AMQP Error code to class mapping")
error_lines[0] = error_lines[0].replace('               ',
                                        'AMQP_ERRORS = {')
error_lines[-1] = error_lines[-1].replace(',', '}')
output += error_lines

# Get the amqp class list so we can sort it
class_list = list()
for amqp_class in amqp['classes']:
    class_list.append(amqp_class['name'])

# Sort them alphabetically
class_list.sort()



newline()
comment("AMQP Classes and Methods")

# First line prefix
prefix = "FRAMES = {"
base_width = 9

# Protocol Class and Methods Dict
for amqp_class in class_list:

    # Make sure we're not hitting a deprecated class like Access
    if amqp_class not in CODEGEN_IGNORE_CLASSES:

        # find the offset in our amqp classes list
        for offset in xrange(0, len(amqp['classes'])):
            if amqp['classes'][offset]['name'] == amqp_class:
                break

        # Create our class prefix
        class_prefix = "%i:{" % amqp['classes'][offset]['id']

        # Append our class line
        newline("%s%s\"name\": \"%s\"," % (prefix, class_prefix, amqp_class))

        # Replace our previous prefix with spaces
        if prefix:
            prefix = "".join([" " for padding in xrange(0, len(prefix))])

        # Create the methods prefix for this AMQP class
        methods_prefix = "\"methods\": {"

        # Iterate through each method
        for method in amqp['classes'][offset].get('methods', []):

            # Build our method prefix
            method_prefix = "%s%i: {" % (methods_prefix,
                                          method['id'])

            # Replace the methods prefix with spaces
            if methods_prefix:
                methods_prefix = \
                    "".join([" " for padding in \
                            xrange(0, len(methods_prefix))])

            # Add our method name line
            newline("%s\"name\": \"%s\"," % \
                    (method_prefix,
                     method['name']),
                    len(prefix) + len(class_prefix))

            # Parameters
            params_prefix = "\"args\": ["

            # Iterate through the parameters adding method parameters lines
            for parameter in method.get('arguments', []):

                # Add our parameter name
                newline("%s{\"name\": \"%s\"," % \
                        (params_prefix,
                         parameter['name']),
                         len(prefix) + len(class_prefix) + len(method_prefix))

                # Replace the methods prefix with spaces
                if params_prefix:
                    params_prefix = \
                        "".join([" " for padding in \
                                xrange(0, len(params_prefix))])

                # Add our parameter type or domain
                newline("%s\"type\": \"%s\"," % \
                        (params_prefix,
                         parameter.get('type',
                                       parameter.get('domain', 'Unknown'))),
                         len(prefix) + len(class_prefix) + len(method_prefix))

                default = parameter.get("default-value", "None")

                if default == 'false':
                    default = False
                elif default == 'true':
                    default = True
                elif default == "" or \
                     default == {} or \
                    default == "None":
                    default = None
                else:
                    try:
                        default = int(default)
                    except ValueError:
                        default = "\"%s\"" % default

                # Add our parameter default
                newline("%s\"default\": %s," % \
                        (params_prefix, default),
                         len(prefix) + len(class_prefix) + len(method_prefix))

                # Close out the parameters
                newline("},",
                        len(prefix) + len(class_prefix) + \
                        len(method_prefix) + len(params_prefix))

            # Close out the method
            if  method.get('arguments', None):
                newline("],",
                        len(prefix) + len(class_prefix) +\
                        len(method_prefix) + len(params_prefix) - 2)

            # Close out the method
            newline("},",
                    len(prefix) + len(class_prefix) + len(method_prefix) - 2)


        # Close out the methods
        newline("},", len(prefix) + len(class_prefix) - 2)

        if  amqp['classes'][offset].get('properties', None):

            # Create the methods prefix for the class properties
            props_prefix = "\"properties\": ["

            # Iterate through each method
            for prop in amqp['classes'][offset]['properties']:

                # Add our parameter name
                newline("%s{\"name\": \"%s\"," % \
                        (props_prefix,
                         prop['name']),
                         len(prefix) + len(class_prefix))

                # Replace the methods prefix with spaces
                if props_prefix:
                    props_prefix = \
                        "".join([" " for padding in \
                                xrange(0, len(props_prefix))])

                # Add our parameter type or domain
                newline("%s \"type\": \"%s\"," % \
                        (props_prefix,
                         prop.get('type', prop.get('domain', 'Unknown'))),
                         len(prefix) + len(class_prefix))

                default = prop.get("default-value", "None")

                if default == 'false':
                    default = False
                elif default == 'true':
                    default = True
                elif default == "" or \
                     default == {} or \
                    default == "None":
                    default = None
                else:
                    try:
                        default = int(default)
                    except ValueError:
                        default = "\"%s\"" % default

                # Add our parameter default
                newline("%s \"default\": %s," % \
                        (props_prefix, default),
                         len(prefix) + len(class_prefix))

                # Close out the properties
                newline("},",
                        len(prefix) + \
                        len(class_prefix) + \
                        len(props_prefix) - 2)

            # Close out the properties
            newline("],", len(prefix) + len(class_prefix) - 2)

        # Close out the class
        newline("},", len(prefix))

# Close out the dict
newline("}", base_width - 2)
newline()

# Create our output string
output_string = '\n'.join(output)

# Clean up the dict line endings
output_string = sub(',\n([ ]*)},', '},', output_string)
output_string = sub('],\n([ ]*)},', ']},', output_string)
output_string = sub('},\n([ ]*)],', '}],', output_string)
for replacement in xrange(0, 2):
    output_string = sub('},\n([ ]*)},', '}},', output_string)
output_string = sub('},\n([ ]*)}', '}}', output_string)
output_string = sub('},\n([ ]*)]', '}]', output_string)

# Spit out the file
with open(CODEGEN_OUTPUT, 'w') as handle:
    handle.write(output_string)

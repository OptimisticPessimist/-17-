from playscript.conv import fountain, pdf

with open('./books/scenario.fountain', encoding='utf-8') as f:
    script = fountain.psc_from_fountain(f.read())

pdf_stream = pdf.psc_to_pdf(script)

with open('./out/scenario.pdf', 'wb') as f:
    f.write(pdf_stream.read())

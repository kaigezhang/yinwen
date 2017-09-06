import subprocess
import app.config as config


def pdf2html(pdf_path):
    fn = pdf_path.split('/')[-1].replace('.pdf', '')
    options = [
        # '--fit-width=%s',
        '--embed cijo',
        '--process-outline=0',
        '--optimize-text=1',
        '--dest-dir=%s/%s' % (config.HTML_DIR, fn),
        '--css-filename=main.css',
        '%s index.html' % pdf_path
    ]
    subprocess.check_call(['pdf2htmlEX'] + options)

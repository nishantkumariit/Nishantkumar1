set -e
cd /tmp/claude-0/-home-user-Nishantkumar1/bfcd13db-6e92-51d7-93f0-7c69b2cf25bb/scratchpad/c9b/build
P=/usr/local/lib/python3.11/dist-packages/pypandoc/files/pandoc
O=/root/.claude/skills/synced/78c4afc9-330c-4c26-a6b5-3cb5706540ac_95ec6797-5b32-4bd7-ba7a-7deff46f9727/docx/scripts
$P blocks.md -f markdown -t docx --reference-doc=orig.docx -o blocks.docx
mkdir -p bl work
unzip -q -o blocks.docx -d bl
unzip -q -o orig.docx -d work
python3 $O/merge_runs.py work/ | tail -1
python3 edit9b.py
python3 ../../c7/schemafix.py
rm -f ch9_out.docx; (cd work && zip -qXr ../ch9_out.docx '[Content_Types].xml' _rels docProps word)
python3 $O/office/validate.py ch9_out.docx 2>&1 | grep -i 'fail\|all validations' | head
mkdir -p pdf; timeout 300 python3 $O/office/soffice.py --headless --convert-to pdf --outdir pdf ch9_out.docx >/dev/null 2>&1
pdfinfo pdf/ch9_out.pdf | grep Pages; pdftotext -layout pdf/ch9_out.pdf pdf/ch9_out.txt

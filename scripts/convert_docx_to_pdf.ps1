param(
    [string]$inputDocx,
    [string]$outputPdf
)

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open((Resolve-Path $inputDocx).Path)
    $outPath = [System.IO.Path]::GetFullPath($outputPdf)
    $doc.SaveAs([ref]$outPath, [ref]17)
    $doc.Close()
    $word.Quit()
    Write-Output "SUCCESS: Converted $inputDocx to $outputPdf"
} catch {
    Write-Error $_
    if ($word) { $word.Quit() }
    exit 1
}

# Powershell implementation.
write-host $PWD
$files = Get-ChildItem $PWD  | Where-Object { ! $_.PSIsContainer } | Select-Object Name
$out = ''
foreach ($file in $files) {
    $out += $file.name.PadRight(20)
}
Write-Host $out
$folders = Get-ChildItem $PWD  | Where-Object { $_.PSIsContainer } | Select-Object Name
$out = ''
foreach ($folder in $folders) {
    $out += $folder.name.PadRight(20)
}
Write-Host $out

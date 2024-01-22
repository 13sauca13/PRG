# Listar los discos duros
Get-Disk

# Comprobar las particiones del disco
Get-Partition -DiskNumber 0

# Reducir el tamaño del disco en 1Gb
Resize-Partition -DiskNumber 0 -PartitionNumber 2 -Size 48.42GB

# Crear una nueva partición que emplee el tamaño liberado
New-Partition -DiskNumber 0 -UseMaximumSize -DriveLetter E -MbrType IFS

# Formatear la unidad E y nombrarla como AD
Format-Volume -DriveLetter E -FileSystem NTFS -NewFileSystemLabel "AD"
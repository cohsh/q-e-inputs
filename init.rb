require 'open-uri'
require 'zlib'
require 'archive/tar/minitar'

dir_cache = '.cache/'
file_tar = 'sg15_oncv_upf_2020-02-06.tar.gz'
dir_pseudo = 'pseudos/sg15'

if ! File.directory?(dir_cache)
  Dir.mkdir(dir_cache)
end

if ! File.directory?(dir_pseudo)
  # Download SG15 Optimized Norm-Conserving Vanderbilt (ONCV) pseudopotentials.
  # M. Schlipf and F. Gygi, Computer Physics Communications 196, 36 (2015).
  url_base = 'http://www.quantum-simulation.org/potentials/sg15_oncv/'
  URI.open(url_base + file_tar) do |res|
    IO.copy_stream(res, dir_cache + file_tar)
  end

  Zlib::GzipReader.open(dir_cache + file_tar) do |gz|
    Archive::Tar::Minitar::unpack(gz, dir_pseudo)
  end

end

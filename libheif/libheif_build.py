from cffi import FFI

ffibuilder = FFI()

with open("libheif/heif.h") as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    "_libheif_cffi",
    """
     #include "libheif/heif.h"
    """,
    include_dirs=["/usr/local/include", "/usr/include"],
    library_dirs=["/usr/local/lib", "/usr/lib", "/lib"],
    libraries=["heif"],
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

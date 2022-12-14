def run(target, source, env):
    src = source[0]
    dst = target[0]
    f = open(src, "r", encoding="utf-8")
    g = open(dst, "w", encoding="utf-8")

    g.write(
        """/* THIS FILE IS GENERATED DO NOT EDIT */
#ifndef GDNATIVE_INTERFACE_DUMP_H
#define GDNATIVE_INTERFACE_DUMP_H

#ifdef TOOLS_ENABLED

#include "core/io/file_access.h"
#include "core/string/ustring.h"

class GDNativeInterfaceDump {
	private:
        static constexpr char const *gdnative_interface_dump ="""
    )
    for line in f:
        g.write('"' + line.rstrip().replace('"', '\\"') + '\\n"\n')
    g.write(";\n")

    g.write(
        """
    public:
        static void generate_gdnative_interface_file(const String &p_path) {
            Ref<FileAccess> fa = FileAccess::open(p_path, FileAccess::WRITE);
            CharString cs(gdnative_interface_dump);
            fa->store_buffer((const uint8_t *)cs.ptr(), cs.length());
        };
};

#endif // TOOLS_ENABLED

#endif // GDNATIVE_INTERFACE_DUMP_H
"""
    )
    g.close()
    f.close()


if __name__ == "__main__":
    from platform_methods import subprocess_main

    subprocess_main(globals())

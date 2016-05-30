# mcv
A simple, command-line utility for reading the Minecraft launcher version manifest.
Allows you to easily get the latest Minecraft version identifiers and associated metadata (like JAR URL, checksum, and size).

You can use the `--help` argument for detailed help, but a list of basic example uses follows.

### Getting the latest version IDs
```bash
$ ./mcv.py latest release
1.9.4

$ ./mcv.py latest snapshot
16w21b
```

### Getting metadata for a version
```bash
$ ./mcv.py meta 1.9.4 server url
https://launcher.mojang.com/mc/game/1.9.4/server/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar

$ ./mcv.py meta 1.9.4 server sha1
edbb7b1758af33d365bf835eb9d13de005b1e274

$ ./mcv.py meta 1.9.4 server size
9399053
```

For the version specifier, "latest-release" and "latest-snapshot" can be used instead of a specific version ID, like so:
```bash
$ ./mcv.py meta latest-release server url
https://launcher.mojang.com/mc/game/1.9.4/server/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar
```

### Staging server
Mojang has a staging server where new releases are often deployed a bit before they are actually released.
mcv supports reading from the staging version manifest by specifying the `--staging` flag, like so:
```bash
$ ./mcv.py --staging latest snapshot
16w21b

$ ./mcv.py --staging meta 16w21b server url
https://launcher.mojang.com/mc-staging/game/16w21b/server/6dedac03d0fbfbcabe8ef09b170a577a9f72c6f8/server.jar
```

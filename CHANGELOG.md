## [1.2.0](https://github.com/YWRBSB/catalog/compare/v1.1.0...v1.2.0) (2026-09-15)

### Features

* Added detailed book endpoint ([5fd8db2](https://github.com/YWRBSB/catalog/commit/5fd8db24764916688cbcc04c53752ffc10b07c31))

## [1.1.0](https://github.com/YWRBSB/catalog/compare/v1.0.1...v1.1.0) (2026-09-15)

### Features

* add book detail endpoint ([0ce0a87](https://github.com/YWRBSB/catalog/commit/0ce0a8772d69e95b64566a7766e9ed527715885a))

## [1.0.1](https://github.com/YWRBSB/catalog/compare/v1.0.0...v1.0.1) (2026-09-15)

### Bug Fixes

* publish production image to ghcr ([531da26](https://github.com/YWRBSB/catalog/commit/531da261175d1a28a51b3a21ba52ca69437d0b35))

{
    "branches": [
        "main"
    ],
    "plugins": [
        [
            "@semantic-release/commit-analyzer",
            {
                "preset": "conventionalcommits"
            }
        ],
        [
            "@semantic-release/release-notes-generator",
            {
                "preset": "conventionalcommits"
            }
        ],
        [
            "@semantic-release/changelog",
            {
                "changelogFile": "CHANGELOG.md"
            }
        ],
        "@semantic-release/github",
        [
            "@semantic-release/git",
            {
                "assets": [
                    "CHANGELOG.md"
                ],
                "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
            }
        ]
    ]
}

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

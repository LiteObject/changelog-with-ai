```markdown
# Changelog

This document provides a detailed list of changes and updates made to the LiteObject/changelog-with-ai project. It aims to help users and developers stay informed about new features, improvements, bug fixes, and other significant alterations.

## [Unreleased]

## [Current Release]

### Refactor

- Improved code organization by separating GitHub API interactions into a new `git_client` module, enhancing maintainability and readability. This change aims to make the codebase more organized and easier to work with, especially for those dealing with GitHub API interactions.
- Moved token retrieval to the main block for improved security and centralized access control. This update prioritizes the security of the application, ensuring that sensitive information such as access tokens are handled in a more secure manner.
- Updated function calls to use the new `git_client` module for fetching commit messages, pull request changes, and descriptions. This modification ensures that all GitHub API related processes are streamlined through one module, improving efficiency and consistency in the codebase.

### Chores

- Updated `.github/CODEOWNERS` to assign ownership to the `LiteObject` team. This change specifies who is responsible for reviewing and managing the code, ensuring that the right people are notified for pull requests and code changes.

### Pull Request Details

- **PR Number**: 4
- **Contributor**: LiteObject
- **Title**: Update method signatures
- **Date Merged**: 2024-03-05
- **Changes**: 110 additions and 120 deletions across 3 files.

For more details, please visit [PR #4](https://github.com/LiteObject/changelog-with-ai/pull/4).

---

For the latest updates and more information, please visit the [LiteObject/changelog-with-ai repository](https://github.com/LiteObject/changelog-with-ai).
```
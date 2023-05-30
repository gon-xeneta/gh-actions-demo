import os
from githubgql import githubgql

QUERY = """
query{
  search(query: "\"Ref BOX-*\" is:open is:pr repo:xeneta/pi -review:approved sort:created-asc", type: ISSUE, first: 100) {
    issueCount
    edges {
      node {
        ... on PullRequest {
          number
          title
          repository {
            nameWithOwner
          }
          createdAt
          url
          changedFiles
          additions
          deletions
          reviewRequests(first: 100) {
            nodes {
              requestedReviewer {
                ... on User {
                  name
                  login
                }
              }
            }
          }
        }
      }
    }
  }
}
"""

token = os.environ.get('BOT_TOKEN', "GITHUB_TOKEN")

result = githubgql.graphql(QUERY, token)

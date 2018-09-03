import {InMemoryCache} from 'apollo-cache-inmemory/lib/index'
import {HttpLink} from 'apollo-link-http/lib/index'
import {ApolloClient} from 'apollo-client/index'
import {ApolloLink} from 'apollo-link'
import fetch from 'unfetch'

const httpLink = new HttpLink({
  uri: process.env.NODE_ENV !== 'production' ? 'http://localhost:8000/api/graphql/' : '/api/graphql/',
  credentials: 'include',
  fetch: fetch,
  headers: {
    'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*=\s*([^;]*).*$)|^.*$/, '$1')
  }
})

const consoleLink = new ApolloLink((operation, forward) => {
  console.log(`starting request for ${operation.operationName}`);

  return forward(operation).map((data) => {
    console.log(`ending request for ${operation.operationName}`);

    return data
  })
})

const composedLink = ApolloLink.from([consoleLink, httpLink]);

// Create the apollo client
export default new ApolloClient({
  link: composedLink,
  // link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true
})

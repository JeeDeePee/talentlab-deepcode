import {InMemoryCache} from 'apollo-cache-inmemory/lib/index'
import {HttpLink} from 'apollo-link-http/lib/index'
import {ApolloClient} from 'apollo-client/index'

const httpLink = new HttpLink({
  uri: process.env.NODE_ENV !== 'production' ? 'http://localhost:8000/api/graphql/' : '/api/graphql/',
  credentials: 'include',
  headers: {
    'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*=\s*([^;]*).*$)|^.*$/, '$1')
  }
})

// Create the apollo client
export default new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true
})

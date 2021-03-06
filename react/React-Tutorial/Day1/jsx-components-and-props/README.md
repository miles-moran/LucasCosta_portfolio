# JSX, Components and Props

Demo:

![Demo](./demo.gif)

## JSX

- Introducing [JSX](https://reactjs.org/docs/introducing-jsx.html)

1. JSX looks like HTML (although its not). Its available by importing from 'react'

2. Optional, not required

 ```js
 // Ex of react without JSK
 React.createElement('h1', /* ... h1 children ... */)
 ```

3. You cannot render more than 1 JSX element next to each other (in the same render return)

4. You CAN however, wrap elements within other elements. Ex: a `<div>` within another `<div>`

```js
// Allowed:
render() {
  return (
    <div>
      <p>Hello world!! I am wrapped</p>
      <h3> I am still wrapper </h3>
    </div>
  )
}

// Not allowed
render() {
  return (
    <p>Hello world!! I am wrapped</p>
    <h2>I am not wrapped</h2>
  )
}
```

5. You can only render built-in DOM components such as `<div>, <p>, <li>, etc` but you can create your own components with any name you want.

6. [JSX In-Depth](https://reactjs.org/docs/jsx-in-depth.html#why-jsx)

Some important points from the link above:

- User-Defined Components Must Be Capitalized

- Props Default to “True”

- Spread Attributes

## Components and Props

[Documentation - Click me!](https://reactjs.org/docs/components-and-props.html)

1. Components use XML-like syntax (JSX)

2. Can maintain its own internal state

3. Simple functional component:

```js
function MyAwesomeFirstComponent() {
  return (
    <div>
      <p>How you doin... </p>
    </div>
  );
}
```

``` js
// Component declaration with arrow function
const MyAwesomeFirstComponent = () => <div><p>How you doin... </p></div>
```

4. Render it:

```js
ReactDOM.render(
  <MyAwesomeFirstComponent />,
  document.getElementById("root")
);
```

5. You can also put this component in a separate file, export it, and import it in your main file

```js
// MyAwesomeFirstComponent.js
import React from 'react';

const MyAwesomeFirstComponent = () => <div><p>How you doin... </p></div>

export default MyAwesomeFirstComponent;

// index.js
import MyAwesomeFirstComponent from './components/MyAwesomeFirstComponent.js'
```

6. Components can take JSX attributes, called props (short for properties)
```js
const MyAwesomeFirstComponent = (props) => <div><p>How you doin... {props.name} </p></div>

ReactDOM.render(
  <MyAwesomeFirstComponent name="Thanos" />,
  document.getElementById('root')
);
```

- note that the component must take a `props` argument for this to work.

7. Components can refer to other components:
```js
// index.js
ReactDOM.render(
  <MyAwesomeFirstComponent />,
  document.getElementById('root')
);

// MyAwesomeFirstComponent.js
import HelloEveryone from './HelloEveryone.js';

const MyAwesomeFirstComponent = () => (
  <div>
    <HelloEveryone name="Thanos" />
    <HelloEveryone name="Iron Man" />
    <HelloEveryone name="Dr Strange" />
  </div>
)

// HelloEveryone.js
const HelloEveryone = (props) => (
  <div><p>How you doin... {props.name} </p></div>
)
```

8. Passing multiple props

```js
// index.js
ReactDOM.render(
  <MyAwesomeFirstComponent />,
  document.getElementById('root')
);

// MyAwesomeFirstComponent.js
const superPeople = [
  {
    name: 'Thanos',
    power: 'The Snap!'
  },
  {
    name: 'Iron Man',
    power: 'Intelligence x 3000'
  },
  {
    name: 'Dr Strange',
    power: 'the Time Stone'
  }
];
const restaurants = ['Cosmic Stones Wings', 'BK', 'Rye of Agamotto']


const MyAwesomeFirstComponent = () => (
  <div>
    <HelloEveryone
      superPeople={superPeople}
      restaurants={restaurants}
    />
  </div>
)

// HelloEveryone.js
const HelloEveryone = (props) => {
  const listItems = props.superPeople.map((person) => (
    <p key={person.name}>{person.name} has {person.power}</p>)
  );
  return (
    <div>
      <h3>Super people</h3>
      {listItems}
      <h3> Restaurants </h3>
      {props.restaurants.map(restaurant => <p key={restaurant}>{restaurant}</p>)}
    </div>
  );
}
```

9. Props are Read-Only

[Read here](https://reactjs.org/docs/components-and-props.html#props-are-read-only)

Because props are not mutable, we cannot change the view directly. For this example, we are going to rerender the app whenever onClick is called: (React is not used this way - we're only doing this to understand this concept)

```js
// index.js
const handleClick = () => {
  ReactDOM.render(
    <MyAwesomeFirstComponent />,
    document.getElementById('root')
  );
}

handleClick(); // rendering when browser first starts
```

10. Having some fun:

``` js
// index.js
const handleClick = () => {
  ReactDOM.render(
    <MyAwesomeFirstComponent
      onClick={handleClick}/>,
    document.getElementById('root')
  );
}

handleClick(); // rendering when browser first starts

// MyAwesomeFirstComponent.js
const MyAwesomeFirstComponent = (props) => (
  <div>
    <HelloEveryone
      superPeople={superPeople}
    />
    <Restaurants
      restaurants={restaurants}
    />
    <Randomizer
      superPeople={superPeople}
      restaurants={restaurants}
      onClick={props.onClick}
    />
  </div>
)

// HelloEveryone.js
const HelloEveryone = (props) => {
  const listItems = props.superPeople.map((person) => (
    <p key={person.name}>{person.name} has {person.power}</p>)
  );
  return (
    <div>
      <h3>Super people</h3>
      {listItems}
    </div>
  );
}

// Restaurants.js
const Restaurants = (props) => (
  <div>
    <h3>Best Restaurants:</h3>
    {props.restaurants.map(restaurant => <p key={restaurant}>{restaurant}</p>)}
  </div>
);

// Randomizer.js
let randomPerson;
let randomRestaurant;

const randomize = (props) => {
  const { superPeople, restaurants } = props;
  randomPerson = superPeople[Math.floor(Math.random() * superPeople.length)];
  randomRestaurant = restaurants[Math.floor(Math.random() * restaurants.length)];
  props.onClick();
}

const Randomizer = (props) => {
  return (
    <div>
      <h3>Randomizer</h3>
      <button onClick={() => randomize(props)}>
        Click me
      </button>
      {(randomPerson && randomRestaurant) &&
        <h4>{randomPerson.name} likes to eat at {randomRestaurant}</h4>}
    </div>
  );
}
```

import React from 'react';
import Accordion from './Accordion';

// Example usage
const App = () => {
  const accordionItems = [
    { title: 'Section 1', body: 'Section 1 Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae corporis perspiciatis tempora deserunt, omnis nulla saepe nemo minima voluptates magni' },
    { title: 'Section 2', body: 'Section 2 Section 1 Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae corporis perspiciatis tempora deserunt, omnis nulla saepe nemo minima voluptates magni' },
    { title: 'Section 3', body: 'Section 3 Section 1 Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae corporis perspiciatis tempora deserunt, omnis nulla saepe nemo minima voluptates magni' },
  ];

  return (
    <div>
      <h1>React Accordion</h1>
      {/* Render Accordion component with items */}
      <Accordion items={accordionItems} />
    </div>
  );
};

export default App;

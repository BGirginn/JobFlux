import React from 'react';
import { render, screen } from '@testing-library/react';
import SearchForm from '../../src/components/search/SearchForm';

describe('SearchForm', () => {
  it('renders job title and location input fields', () => {
    render(<SearchForm />);
    expect(screen.getByLabelText(/Job Title/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Location/i)).toBeInTheDocument();
  });

  it('renders a search button', () => {
    render(<SearchForm />);
    expect(screen.getByRole('button', { name: /Search/i })).toBeInTheDocument();
  });
});

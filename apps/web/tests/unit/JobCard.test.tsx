import React from 'react';
import { render, screen } from '@testing-library/react';
import JobCard from '../../src/components/search/JobCard';

describe('JobCard', () => {
  const mockJob = {
    title: 'Software Engineer',
    company: 'Tech Corp',
    location: 'San Francisco',
    description: 'Develop and maintain software.',
  };

  it('renders job details correctly', () => {
    render(<JobCard {...mockJob} />);
    expect(screen.getByText(mockJob.title)).toBeInTheDocument();
    expect(screen.getByText(`${mockJob.company} - ${mockJob.location}`)).toBeInTheDocument();
    expect(screen.getByText(mockJob.description)).toBeInTheDocument();
  });
});

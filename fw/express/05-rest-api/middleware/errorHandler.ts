import { ErrorRequestHandler } from 'express';

interface HttpError {
  statusCode?: number;
  message?: string;
}

const errorHandler: ErrorRequestHandler = (err: HttpError, _req, res, _next) => {
  const statusCode = err.statusCode ?? 500;
  const message = err.message ?? 'Internal Server Error';
  if (statusCode === 500) console.error(err);
  res.status(statusCode).json({ statusCode, message });
};

export default errorHandler;

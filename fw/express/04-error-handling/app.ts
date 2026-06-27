import express, { Request, Response, NextFunction, ErrorRequestHandler } from 'express';

const app = express();
app.use(express.json());

class HttpError extends Error {
  constructor(public statusCode: number, message: string) {
    super(message);
    this.name = 'HttpError';
  }
}

app.get('/ok', (_req: Request, res: Response) => {
  res.json({ message: '정상' });
});

app.get('/sync-error', (_req: Request, _res: Response, next: NextFunction) => {
  try {
    throw new HttpError(400, '잘못된 요청');
  } catch (err) {
    next(err);
  }
});

app.get('/async-error', async (_req: Request, _res: Response, next: NextFunction) => {
  try {
    await Promise.reject(new HttpError(404, '리소스를 찾을 수 없음'));
  } catch (err) {
    next(err);
  }
});

// ErrorRequestHandler: (err: any, req, res, next) => void
// 파라미터가 반드시 4개여야 Express가 에러 미들웨어로 인식
const errorHandler: ErrorRequestHandler = (err, _req, res, _next) => {
  if (err instanceof HttpError) {
    res.status(err.statusCode).json({ statusCode: err.statusCode, message: err.message });
  } else {
    console.error(err);
    res.status(500).json({ statusCode: 500, message: 'Internal Server Error' });
  }
};

app.use(errorHandler);

app.listen(3000, () => console.log('http://localhost:3000'));

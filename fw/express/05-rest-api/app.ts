import express, { Request, Response, NextFunction } from 'express';
import postsRouter from './routes/posts';
import errorHandler from './middleware/errorHandler';

const app = express();
app.use(express.json());

app.use((req: Request, _res: Response, next: NextFunction) => {
  console.log(`${req.method} ${req.path}`);
  next();
});

app.use('/posts', postsRouter);
app.use(errorHandler);

const PORT = process.env.PORT ?? 3000;
app.listen(PORT, () => console.log(`http://localhost:${PORT}`));

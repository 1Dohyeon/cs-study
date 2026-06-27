import express, { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.get('/', (_req: Request, res: Response) => {
  res.send('Hello Express');
});

// Request<Params, ResBody, ReqBody, Query> 제네릭으로 타입 지정
app.get('/users/:id', (req: Request<{ id: string }>, res: Response) => {
  const { id } = req.params; // string 타입으로 추론됨
  res.json({ userId: id });
});

app.get('/search', (req: Request<{}, {}, {}, { q?: string }>, res: Response) => {
  const { q } = req.query; // string | undefined
  res.json({ keyword: q });
});

interface CreateUserBody {
  name: string;
  email: string;
}

app.post('/users', (req: Request<{}, {}, CreateUserBody>, res: Response) => {
  // req.body가 any 대신 CreateUserBody로 추론됨
  res.status(201).json({ created: req.body });
});

app.listen(3000, () => console.log('http://localhost:3000'));

import { Router, Request, Response, NextFunction } from 'express';
import { auth } from '../middleware/auth';

const router = Router();

interface Post {
  id: number;
  title: string;
  content: string;
}

interface CreatePostBody {
  title: string;
  content: string;
}

let posts: Post[] = [{ id: 1, title: 'Express 입문', content: '미들웨어가 핵심이다' }];
let nextId = 2;

router.get('/', (_req: Request, res: Response) => {
  res.json(posts);
});

router.get('/:id', (req: Request<{ id: string }>, res: Response, next: NextFunction) => {
  const post = posts.find(p => p.id === Number(req.params.id));
  if (!post) { next({ statusCode: 404, message: '포스트를 찾을 수 없음' }); return; }
  res.json(post);
});

router.post('/', auth, (req: Request<{}, {}, CreatePostBody>, res: Response, next: NextFunction) => {
  const { title, content } = req.body;
  if (!title || !content) { next({ statusCode: 400, message: 'title과 content는 필수' }); return; }
  const post: Post = { id: nextId++, title, content };
  posts.push(post);
  res.status(201).json(post);
});

router.put(
  '/:id',
  auth,
  (req: Request<{ id: string }, {}, Partial<CreatePostBody>>, res: Response, next: NextFunction) => {
    const idx = posts.findIndex(p => p.id === Number(req.params.id));
    if (idx === -1) { next({ statusCode: 404, message: '포스트를 찾을 수 없음' }); return; }
    posts[idx] = { ...posts[idx], ...req.body };
    res.json(posts[idx]);
  },
);

router.delete('/:id', auth, (req: Request<{ id: string }>, res: Response, next: NextFunction) => {
  const idx = posts.findIndex(p => p.id === Number(req.params.id));
  if (idx === -1) { next({ statusCode: 404, message: '포스트를 찾을 수 없음' }); return; }
  posts.splice(idx, 1);
  res.status(204).send();
});

export default router;
